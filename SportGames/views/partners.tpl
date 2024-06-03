% rebase('layout.tpl', title=title, year=year)

<div class="container">
    <h1 class="text-center">Parthners company</h1>

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
                                <p><strong>Email:</strong> <a href="mailto:{{ company['email'] }}">{{ company['email'] }}</a></p>
                                <p><strong>Phone:</strong> {{ company['телефон'] }}</p>
                                <p><strong>Details of the partnership:</strong></p>
                                <p>Start date:: {{ company['детали_партнерства']['дата_начала'] }}</p>
                                <p>Term of the contract: {{ company['детали_партнерства']['срок_контракта'] }} года</p>
                                <p>Type of contract: {{ company['детали_партнерства']['тип_контракта'] }}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        % end
    </div>

    <div class="input_container col-xs-6 col-sm-4 thumbnail">
        <form id="input_company_form" action="/parthners" method="post" action="/action_page.php" required name="myForm">
            <p><input type="text" size="80" name="name" placeholder="Name"></p>
            <p><input type="text" size="80" name="email" placeholder="Email"></p>
            <p><input type="text" size="80" name="nелефон" placeholder="Telephone"></p>
            <p><input type="text" size="80" name="дата_начала" placeholder="Date"></p>
            <p><input type="text" size="80" name="срок_контракта" placeholder="Term of the contract"></p>
		    <p><input type="" size="80" name="тип_контракта">Type of the contract</p>
            <p><input type="submit" value="Send" class="btn btn-default"></p>
        </form>
    </div>
</div>