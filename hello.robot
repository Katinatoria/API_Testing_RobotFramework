*** Settings ***
Library   tests.py


*** Test Cases ***
Count character
    [Documentation]      Проверяем, что заявленное количество персонажей в описании соответсвует фактическому
    ...                  Ожидается, что количество персонажей совпадет с числом 826
    ${count}=  get_all_char
    Should Be Equal  ${count}  ${826}


Direct geocoding
    [Documentation]      Прямое геокодирование
    ...                  Ожидается, что функция вернет значения lat и lon ('59.79995795', '30.609312250000002')
    ${geocod}=  geocode
    ${list} =    Create List    59.79995795    30.609312250000002
    Should Be Equal  ${geocod}  ${list}


Reverse geocoding
    [Documentation]      Обратное геокодирование
    ...                  Ожидается, что функция вернет значение Mudemba
    ${addr_city}=  geocode_rev
    Should Be Equal  ${addr_city}  Mudemba
