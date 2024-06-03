% rebase('layout.tpl', title=title, year=year)

<div class="container">
    <h1 class="text-center">Partner Companies in Sports</h1>
    <div class="row">
        % for company in partner_companies['партнерские_компании_в_сфере_спорта']:
            <div class="col-md-6 col-sm-12">
                <div class="panel-group">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <h4 class="panel-title">
                                <a data-toggle="collapse" href="#collapse{{ company['id'] }}">{{ company['название'] }}</a>
                            </h4>
                        </div>
                        <div id="collapse{{ company['id'] }}" class="panel-collapse collapse collapse">
                            <div class="panel-body">
                                <p>{{ company['описание'] }}</p>
                                <p><strong>Вебсайт:</strong> <a href="{{ company['вебсайт'] }}" target="_blank">{{ company['вебсайт'] }}</a></p>
                                <p><strong>Email:</strong> <a href="mailto:{{ company['email'] }}">{{ company['email'] }}</a></p>
                                <p><strong>Телефон:</strong> {{ company['телефон'] }}</p>
                                <p><strong>Адрес:</strong> {{ company['адрес']['улица'] }}, {{ company['адрес']['город'] }}, {{ company['адрес']['штат'] }} {{ company['адрес']['индекс'] }}, {{ company['адрес']['страна'] }}</p>
                                <p><strong>Спортивные продукты или услуги:</strong></p>
                                <ul>
                                    % for product in company['спортивные_продукты_или_услуги']:
                                        <li>{{ product }}</li>
                                    % end
                                </ul>
                                <p><strong>Детали партнерства:</strong></p>
                                <p>Дата начала: {{ company['детали_партнерства']['дата_начала'] }}</p>
                                <p>Срок контракта: {{ company['детали_партнерства']['срок_контракта'] }} года</p>
                                <p>Тип контракта: {{ company['детали_партнерства']['тип_контракта'] }}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        % end
    </div>
</div>