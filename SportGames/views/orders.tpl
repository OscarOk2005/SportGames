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

    <h1> Add an order</h1>
    <div class="input_container col-xs-6 col-sm-4 thumbnail">
        <form action="/orders" method="post" action="/action_page.php" required name="myForm">
                <p><input type="text" size="50" name="Customer" pattern="[a-zA-Z\-]{4,}" title="Enter first and last name with a space in Latin characters" placeholder="Your surname and name" ></p>
                <p><input type="text" size="50" name="Product" pattern="[a-zA-Z\-]{2,}" title="Enter product name in Latin characters" placeholder="Your product"  ></p>
                <p><input type="text" size="50" name="Phone" pattern="[0-9\+]{2,}" title="Phone can consist of numbers and +" placeholder="Your phone" ></p>
                <p><input type="text" size="50" name="Address" pattern="[a-zA-Z\-.]{12,}"  title="Enter your address in Latin characters, - and ." placeholder="Your address"  \></p>
		        <p><input id="html" size="50" name="Delivery" type="checkbox">Home delivery</p>
                <p><input type="submit" value="Send" class="btn btn-default"></p>
            </div>
        </form>
    </div>
</div>