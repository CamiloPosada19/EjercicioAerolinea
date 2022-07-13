import time
from Pages.BasePage import BasePage
from datetime import date

basePage = BasePage()

class VuelingPage(BasePage):
    # -----------------------------------Locators origen y destino----------------------------------------------------
    __btn_cookies_xpath = "//button[@class='button raised blue'][contains(.,'Acepta todas las cookies')]"
    __inpt_origen_xpath = "//input[@type='text'][contains(@id,'TextBoxMarketOrigin1')]"
    __dropdown_origen_xpath = "//li[contains(.,'Barcelona, España (BCN)')]"
    __dropdown_destino_xpath = "//li[@class='directo'][contains(.,'Madrid, España (MAD)')]"
    # ----------------------------------Locators para el calendario-----------------------------------------------------
    __text_calendar_xpath = "//span[@class='icoSpriteB icoSprite_bf icoPlaneIda_yellow_bf']"
    __text_dateFin_xpath = "(//a[@class='ui-state-default'][contains(.,'29')])[1]"
    __div_contenedor_fuera = "//div[contains(@class,'vy-contain-footer__newsletter')]"
    # -----------------------------------Verificar ventana principal----------------------------------------------------
    __title_buscar_vuelo_xpath = "//h2[contains(.,'Busca un vuelo:')]"
    btn__buscar_vuelo_xpath = "//div[@class='column_4 txtAlignMiddle paddingBottom20'][contains(.,'Buscar vuelos')]"
    select__adults_xpath = "//div[@class='column_4 txtAlignMiddle paddingBottom20'][contains(.,'Buscar vuelos')]"
    #-----------------------------------SelectorAdultos-----------------------------------------------------------------
    __select__dos_adultos_xpath="//a[@data-n-adults='2']"
    __select_bebes_xpath="//select[contains(@name,'CHD')]"
    #---------------------------------BotonBuscarVuelos-----------------------------------------------------------------
    __btn_buscar_vuelos_xpath="//a[contains(@id,'btnClickToSearchNormal')]"
    __acceso_denegado_xpath="//h1"

    # Methods

    def entrarEntorno(self, entorno):
        entorno = BasePage.getData(self, "entornoDev", "envPro", f"{entorno}")
        basePage.openBrowser(entorno)

    def aceptarPoliticaDeCookies(self):
        basePage.click(self.__btn_cookies_xpath)

    def seleccionarVuelosBarcelonaMaDird(self):
        basePage.click(self.__inpt_origen_xpath)
        basePage.scroll_to_element(self.__dropdown_origen_xpath)
        basePage.scroll_to_element(self.__dropdown_destino_xpath)

    def validarcalendario(self):
        basePage.validate_text(self.__text_calendar_xpath, "Fecha de ida")

    def seleccionarFechasDeVuelos(self):
        # Suma de dias
        today = date.today()
        print(type(today))
        diaactual = today.day
        fechaInicio = diaactual + 4
        fechaFin = diaactual + 7
        # Seleccionar fechas de inicio y de fin
        basePage.wait(self.__text_calendar_xpath)
        fecha_de_inicio_xpath = f"(//a[@class='ui-state-default'][contains(.,'{fechaInicio}')])[1]"
        fecha_de_fin_xpath = f"(//a[@class='ui-state-default'][contains(.,'{fechaFin}')])[1]"
        fecha_fin_de_mes_29 = f"(//a[@class='ui-state-default'][contains(.,'1')])[2]"
        basePage.click(fecha_de_inicio_xpath)
        basePage.click(fecha_de_fin_xpath)
        time.sleep(5)
        # Fecha es 29 activar el componente para el dia 1
        # if diaactual==29:
        #    BasePage.click(fecha_fin_de_mes_29)

    def verificarventanaPrincipal(self):
        basePage.validate_text(self.btn__buscar_vuelo_xpath, "Buscar vuelos")
        basePage.validate_element_is_visible(self.btn__buscar_vuelo_xpath)
        basePage.validate_element_is_visible(self.select__adults_xpath)

    def selectAdultos(self,adultos):
        select__dos_adultos_xpath = f"//a[@data-n-adults='{adultos}']"
        basePage.click(select__dos_adultos_xpath)

    def select_bebes(self):
        basePage.select_dropdown(self.__select_bebes_xpath,"1")

    def presionar_buscar_vuelos(self):
        basePage.click(self.__btn_buscar_vuelos_xpath)

    def verficar_texto_acceso_denegado(self):
        basePage.validate_text(self.__acceso_denegado_xpath,"ACCESS DENIED")