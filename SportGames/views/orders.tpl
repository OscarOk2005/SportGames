% rebase('layout.tpl', title=title, year=year)
% for order in data:
	<div>
		<h2>{{order["Number"]}} </h2>
		<p>Заказчик: {{order["Customer"]}}</p>
		<p>Товар: {{order["Product"]}}</p>
		<p>Дата заказа: {{order["Order date"]}}</p>
		% if(order["Delivery"]):
			<p>С доставкой на дом</p>
		% end
	</div>
% end
<h1> Добавить заказ</h1>
<form action="/orders" method="post" action="/action_page.php" required name="myForm">
        <p><input type="text" size="50" name="Customer" placeholder="Your surname and name" ></p>
        <p><input type="text" size="50" name="Product" placeholder="Your product"  ></p>
        <p><input type="text" size="50" name="Phone" placeholder="Your phone" ></p>
        <p><input type="text" size="50" name="Address" placeholder="Your address"  \></p>
		<p><input id="html" size="50" name="Delivery" type="checkbox">Доставка на дом</p>
        <p><input type="submit" value="Send" class="btn btn-default"></p>
</form>




