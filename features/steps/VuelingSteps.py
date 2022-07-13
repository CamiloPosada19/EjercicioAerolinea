from Pages.BasePage import BasePage
from Pages.VuelingPage import *
from Pages.BasePage import *
from behave import use_step_matcher, step, when

vuelingPage = VuelingPage()
basePage = BasePage()
use_step_matcher("re")


@step(u'Entrar al entorno "(?P<entorno>.+)"')
def step_impl(context, entorno):
    vuelingPage.entrarEntorno(entorno)


@step(u'Aceptar politica de cookies')
def step_impl(context):
    vuelingPage.aceptarPoliticaDeCookies()


@step(u'Seleccionar Billete de España a Madrid')
def step_impl(context):
    vuelingPage.seleccionarVuelosBarcelonaMaDird()


@step(u'Validar que el calendario se ha abierto correctamente')
def step_impl(context):
    vuelingPage.validarcalendario()

@step(
    u'Seleccionar la fechas de inicio del vuelo sumandole 4 dias a la fecha actual y la fecha de regreso 3 dias despues')
def step_impl(context):
    vuelingPage.seleccionarFechasDeVuelos()


@step(u'Verificar que el boton buscar vuelos esta activo junto con los componentes de adultos y ninos')
def step_impl(context):
    vuelingPage.verificarventanaPrincipal()

@step(u'Seleccionar "(?P<adultos>.+)" adultos')
def step_impl(context,adultos):
    vuelingPage.selectAdultos(adultos)

@step(u'Seleccionar 1 niño')
def step_impl(context):
    vuelingPage.select_bebes()


@step(u'Pulsar el boton buscar')
def step_impl(context):
    vuelingPage.presionar_buscar_vuelos()


@step(u'Verificar que la aplicacion no tiene acceso  a los vuelos en este servidor')
def step_impl(context):
    pass

