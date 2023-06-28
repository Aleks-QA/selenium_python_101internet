<h4>Проект по автоматизации тестирования 101internet</h4>
<li>Заполняем и отправляем заявку для каждого типа подключения</li>
<li>В процессе теста проверяем, что у всех отправленных заявок требуемый статус код</li>
<h4>Запуск тестов</h4>
<li>Установить все зависимости: python -m pip install -r requirements.txt</li>
<li>Отключить антивирус, ему может не понравиться отлов запросов через selenium-wire</li>
<li>Запуск тестов: python -s -m pytest --alluredir=test_results/</li>

<h5>P.S. на <a href="https://github.com/Aleks-QA/selenium_python_101internet/tree/old" target="_blank">второй</a> ветке другой способ реализации</h5>
