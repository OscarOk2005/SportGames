% rebase('layout.tpl', title=title, year=year)

<div class="container" id="container_forms">
    <h1 class="text-center">Orders</h1>

    <div class="row col-md-6">
        % for order in data:
            <div class="col-md-12 col-sm-6">
                <div class="panel-group">
                    <div class="panel panel-default">
                        <div class="panel-heading">
                            <h4 class="panel-title">
                                <a data-toggle="collapse" href="#collapse{{ order['Number'] }}">{{ order["Number"] }}</a>
                            </h4>
                        </div>
                        <div id="collapse{{ order['Number'] }}" class="panel-collapse collapse collapse">
                            <div class="panel-body">
	                            <div>
		                            <h2> </h2>
		                            <p>Customer: {{order["Customer"]}}</p>
		                            <p>Product: {{order["Product"]}}</p>
		                            <p>Date of order: {{order["Order date"]}}</p>
		                            % if(order["Delivery"]):
			                            <p>With home delivery</p>
		                            % end
	                            </div>
                            </div>
                        </div>
                    </div>
                </div>  
            </div>
        % end
    </div>

    <div class="input_container col-xs-4 col-sm-3">
        <h3>Adding a new order</h3>
        <div class="thumbnail">
            <form class="input_form" action="/partners" method="post" action="/action_page.php" required name="myForm">
                <div class="form-group">
                    <input type="text" size="50" name="Customer" placeholder="Your surname and name" >
                </div>
                <div class="form-group">
                    <input type="text" size="50" name="Product" placeholder="Your product">
                </div>
                <div class="form-group">
                    <input type="text" size="50" name="Phone" placeholder="Your phone" >
                </div>
                <div class="form-group">
                    <input type="text" size="50" name="Address" placeholder="Your address">
                </div>
                <div class="form-group">
                    <p><input id="html" size="50" name="Delivery" type="checkbox">Home delivery</p>
                </div>
                <p><input type="submit" value="Send" class="btn btn-default"></p>
            </div>
        </form>
    </div>
</div>