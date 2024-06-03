% rebase('layout.tpl', title=title, year=year)
<div class="container">
    <h1 class="text-center">Orders</h1>

    <div class="row">

        % for order in data:
            <div class="col-md-6 col-sm-12">
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
                <p><input type="text" size="50" name="Customer" placeholder="Your surname and name" ></p>
                <p><input type="text" size="50" name="Product" placeholder="Your product"  ></p>
                <p><input type="text" size="50" name="Phone" placeholder="Your phone" ></p>
                <p><input type="text" size="50" name="Address" placeholder="Your address"  \></p>
		        <p><input id="html" size="50" name="Delivery" type="checkbox">Home delivery</p>
                <p><input type="submit" value="Send" class="btn btn-default"></p>
        </form>
    </div>
</div>


