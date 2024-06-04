% rebase('layout.tpl', title=title, year=year)

<div class="container" id="container_forms">
    <h1 class="text-center">Parthners company</h1>

    <div class="row col-md-6">
        % for company in partner_companies['partner_companies_in_sports_sphere']:
            <div class="col-md-12 col-sm-6">
                <div class="panel-group">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <h4 class="panel-title">
                                <a data-toggle="collapse" href="#collapse{{ company['id'] }}">{{ company['name'] }}</a>
                            </h4>
                        </div>
                        <div id="collapse{{ company['id'] }}" class="panel-collapse collapse collapse">
                            <div class="panel-body">
                                <p>{{ company['description'] }}</p>
                                <p><strong>Email:</strong> <a href="mailto:{{ company['email'] }}">{{ company['email'] }}</a></p>
                                <p><strong>Phone:</strong> {{ company['phone'] }}</p>
                                <p><strong>Details of the partnership:</strong></p>
                                <p>Start date: {{ company['partnership_details']['start_date'] }}</p>
                                <p>Term of the contract: {{ company['partnership_details']['contract_term'] }} years</p>
                                <p>Type of contract: {{ company['partnership_details']['contract_type'] }}</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        % end
    </div>

    <div class="input_container col-xs-4 col-sm-3">
        <h3>Adding a new parthner</h3>
        <div class="thumbnail">
            <form class="input_form" action="/partners" method="post" action="/action_page.php" required name="myForm">
                <div class="form-group">
                  <input type="text" class="form-control input-sm" name="name" placeholder="Name">
                </div>
                <div class="form-group">
                  <input type="email" class="form-control input-sm" name="email" placeholder="Email">
                </div>
                <div class="form-group">
                  <input type="tel" class="form-control input-sm" name="telephone" placeholder="Telephone">
                </div>
                <div class="form-group">
                  <input type="date" class="form-control input-sm" name="date_start" placeholder="Date">
                </div>
                <div class="form-group">
                  <input type="text" class="form-control input-sm" name="contract_term" placeholder="Term of the contract">
                </div>
                <div class="form-group">
                    <label for="con_type">Type of the contract</label>
		            <select class="form-control" id="con_type" name="con_type">
                        <option value="">-- Select an option --</option>
                        <option value="Exclusive">Exclusive</option>
                        <option value="Non-exclusive">Non exclusive</option>
                    </select>
                </div>
                <p><input type="submit" value="Send" class="btn btn-default"></p>
            </div>
        </form>
    </div>
</div>