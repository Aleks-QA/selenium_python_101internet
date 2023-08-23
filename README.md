<h3 tabindex="-1" dir="auto">Проект по автоматизации тестирования 101internet</h3>
<hr>
<h4 dir="auto"><em>О проекте:</em></h4>
<ol>
<li dir="auto">В процессе тестов происходит заполнение и отправка заявки на подключение интернета, тарифы выбираются случайным образом, на каждый тип подключения отправляется по одной заявке:</li>
  <ul dir="auto">
    <li>Заявка на подключение в квартиру</li>
    <li>Заявка на подключение в офис</li>
    <li>Заявка на подключение на дачу</li>
  </ul>
<li dir="auto">В процессе теста проверяем, что у всех отправленных заявок требуемый статус код</li>
</ol>
<hr>

<h4 dir="auto"><em>Для запуска тестов необходимо:</em></h4>
<ol>
  <li>Скачать проект с удаленного репозитория на свой локальный, с помощью команды:<br>
    <code>git clone https://github.com/Aleks-QA/selenium_python_101internet.git</code></li>
  
  <li>Открыть проект на установленной заранее IDE</li>
  
  <li>Создать и активировать виртуальное окружение:</li>
    <code>python -m venv venv</code></li><br>
    <code>venv\Scripts\activate</code></li>
    
  <li>Установить все зависимости: <br>
  <code>python -m pip install -r requirements.txt</code> 
    
  <li>Отключить антивирус, так как ему может не понравиться отлов запросов через библиотеку selenium-wire</li>
  
  <li>Запустить тесты командой:<br><code>python -s -m pytest --alluredir=test_results</code> </li>
  
  <li>Открыть отчет о прохождении тестов командой:<br>
    <code>allure serve test_results/ </code></li>
</ol>

<hr>

<li>Добавлено краткое описание работы проекта в <a href="https://github.com/Aleks-QA/selenium_python_101internet/blob/main/project_description.py" target="_blank">project_description.py</a></li>
<li>На <a href="https://github.com/Aleks-QA/selenium_python_101internet/tree/old" target="_blank">второй</a> ветке другой способ реализации</li>
