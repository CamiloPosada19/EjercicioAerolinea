Feature: Seleccionar un vuelo de ida y de vuelta a barcelona

  Scenario: Comprar un vuelo comprado 4 dias a la fecha actual y 3 dias despues de regreso junto con dos adultos y un nino

    Given Entrar al entorno "uriVueling"
    When Aceptar politica de cookies
    And Seleccionar Billete de España a Madrid
    And Validar que el calendario se ha abierto correctamente
    And Seleccionar la fechas de inicio del vuelo sumandole 4 dias a la fecha actual y la fecha de regreso 3 dias despues
    And Verificar que el boton buscar vuelos esta activo junto con los componentes de adultos y ninos
    And Seleccionar "2" adultos
    And Seleccionar 1 niño
    And Pulsar el boton buscar
    Then Verificar que la aplicacion no tiene acceso  a los vuelos en este servidor

