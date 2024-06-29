import re

from lxml import etree
from pydantic import BaseModel, validator

from spei import types
from spei.utils import to_snake_case, to_upper_camel_case  # noqa: WPS347
from spei.validators import digits

SOAP_NS = 'http://schemas.xmlsoap.org/soap/envelope/'
PRAXIS_NS = 'http://www.praxis.com.mx/'


class Orden(BaseModel):
    id: int
    categoria: types.CategoriaOrdenPago
    op_fecha_oper: int
    op_folio: str
    op_monto: str
    op_tp_clave: types.TipoPagoOrdenPago
    op_cve_rastreo: str
    op_estado: types.EstadoOrdenPago
    op_tipo_orden: types.TipoOrdenPago
    op_prioridad: types.PrioridadOrdenPago
    op_me_clave: types.MedioEntregaOrdenPago
    op_topologia: types.TopologiaOrdenPago = (
        types.TopologiaOrdenPago.notify_on_payment_settlement
    )
    op_usu_clave: str
    # checksum
    op_firma_dig: str
    # origin info
    op_nom_ord: str = None
    op_tc_clave_ord: types.TipoCuentaOrdenPago = None
    op_cuenta_ord: str = None
    op_rfc_curp_ord: str = None
    op_ins_clave_ord: digits(3, 5) = None
    # destination info
    op_nom_ben: str = None
    op_tc_clave_ben: types.TipoCuentaOrdenPago = None
    op_cuenta_ben: str = None
    op_rfc_curp_ben: str = None
    op_ins_clave_ben: digits(3, 5) = None
    # participant info
    op_cuenta_participante_ord: str = None
    op_nom_participante_ord: str = None
    op_rfc_participante_ord: str = None
    # additional destination info
    op_nom_ben_2: str = None
    op_tc_clave_ben_2: types.TipoCuentaOrdenPago = None
    op_cuenta_ben_2: str = None
    op_rfc_curp_ben_2: str = None
    # concept info
    op_concepto_pago: str = None
    op_concepto_pag_2: str = None
    # additional general info
    op_iva: float = None
    op_ref_numerica: str = None
    op_ref_cobranza: str = None
    op_clave_pago: str = None
    # refunds info
    op_to_clave: int = None
    op_cd_clave: types.TipoDevolucionOrdenPago = None
    # invoice info
    op_info_factura: str = None
    # original info
    op_folio_ori: int = None
    paq_folio_ori: int = None
    op_fecha_oper_ori: int = None
    op_rastreo_ori: str = None
    op_monto_intereses: float = None
    op_monto_ori: float = None
    # beneficiary
    op_indica_ben_rec: int = None
    # codi origin info
    op_num_cel_ord: int = None
    op_digito_ver_ord: int = None
    # codi destination info
    op_num_cel_ben: int = None
    op_digito_ver_ben: int = None
    # codi info
    op_folio_codi: str = None
    op_comision_trans: int = None
    op_monto_comision: float = None
    # codi merchant info
    op_cert_comer_env: int = None
    op_digito_ver_comer: int = None
    # karpay system info
    op_fecha_cap: int = None
    op_folio_servidor: int = None
    op_usu_autoriza: str = None
    op_err_clave: types.CodigoError = None
    op_razon_rechazo: str = None
    op_hora_cap: int = None
    op_hora_liq_bm: int = None
    op_hora_liq_sist: int = None
    op_cde: str = None
    op_cuenta_dev: str = None
    op_hora_lectura_host: int = None  # noqa: N815
    op_hora_insercion: int = None
    hr_deposito_acuse_banxico: int = None
    paq_folio: int = None
    ah_ar_clave: int = None
    emp_clave: int = None

    class Config:  # noqa: WPS306, WPS431
        use_enum_values = True

    @validator('op_monto', always=True)
    def set_amount(cls, value):  # noqa: WPS110, N805
        amount = float(value)
        return '{amount:.2f}'.format(amount=amount)

    @validator('op_fecha_oper')
    def op_fecha_oper_must_be_iso_format(cls, value):  # noqa: WPS110, N805
        regex = re.compile(r'^\d{4}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])$')
        if re.findall(regex, str(value)):
            return value

        raise ValueError('must be in YYYYMMDD format')

    def build_xml(self):  # noqa: WPS231, C901
        ordenpago = etree.Element('ordenpago', Id=str(self.id))

        elements = self.dict(
            exclude_none=True,
            exclude={'id', 'categoria', 'op_ins_clave_ord'},
        )

        for element, value in elements.items():  # noqa: WPS110
            if element in self.__fields__:
                if element == 'op_firma_dig':
                    subelement = etree.SubElement(ordenpago, 'opFirmaDig')
                    subelement.text = str(value)
                    continue
                if element == 'op_ins_clave_ben':
                    subelement = etree.SubElement(ordenpago, 'OpInsClave')
                    subelement.text = str(value)
                    continue
                if element == 'op_rastreo_ori':
                    subelement = etree.SubElement(ordenpago, 'opRastreoOri')
                    subelement.text = str(value)
                    continue
                if element == 'op_fecha_oper_ori':
                    subelement = etree.SubElement(ordenpago, 'opFechaOperOri')
                    subelement.text = str(value)
                    continue
                if element == 'op_monto_ori':
                    subelement = etree.SubElement(ordenpago, 'opMontoOri')
                    subelement.text = str(value)
                    continue
                if element == 'op_monto_intereses':
                    subelement = etree.SubElement(ordenpago, 'opMontoInteres')
                    subelement.text = str(value)
                    continue
                if element == 'op_comision_trans':
                    subelement = etree.SubElement(ordenpago, 'opComisionTrans')
                    subelement.text = str(value)
                    continue
                upper_camel_case_element = to_upper_camel_case(element)
                subelement = etree.SubElement(ordenpago, upper_camel_case_element)
                subelement.text = str(value)

        return ordenpago

    @classmethod
    def parse_xml(cls, orden_element, categoria: types.CategoriaOrdenPago):
        orden_data = {
            'id': orden_element.attrib['Id'],
            'categoria': categoria,
        }

        for element in orden_element.getchildren():
            tag = to_snake_case(element.tag)
            if tag in cls.__fields__:
                orden_data[tag] = element.text.strip()
            if tag == 'op_ins_clave':
                orden_data['op_ins_clave_ord'] = element.text

        return cls(**orden_data)
