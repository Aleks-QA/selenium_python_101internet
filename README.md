<h4>Проект по автоматизации тестирования 101internet</h4>
<ol>
<li>Заполняем и отправляем заявку для каждого типа подключения</li>
<ul>
<li>Заявка на подключение интернета в квартиру</li>
<li>Заявка на подключение интернета в офис</li>
<li>Заявка на подключение интернета на дачу</li>
</ul>
<li>В процессе теста проверяем, что у всех отправленных заявок требуемый статус код</li>
</ol>
<h4>Запуск тестов</h4>
<ol>
<li>Установить все зависимости: python -m pip install -r requirements.txt</li>
<li>Отключить антивирус, ему может не понравиться отлов запросов через selenium-wire</li>
<li>Запуск тестов: python -s -m pytest --alluredir=test_results/</li>
</ol>

<h6>P.S. Добавлено небольшое описание работы проекта в <a href="https://github.com/Aleks-QA/selenium_python_101internet/blob/main/project_description.py" target="_blank">project_description.py</a></h6>
<h6>P.S.S. на <a href="https://github.com/Aleks-QA/selenium_python_101internet/tree/old" target="_blank">второй</a> ветке другой способ реализации</h6>
