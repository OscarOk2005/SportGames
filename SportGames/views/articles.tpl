% rebase('layout.tpl', title=title, year=year)

<h1> Adding an article</h1>
<form name="AddingArticles" action="/articles" method="post"  required>
        <p><input type="text" size="50" name="TITLE" autocomplete="off" placeholder="Title of the article" title="The title of the article must contain at least 8 characters (without using special characters)!" ></p>
        <p><textarea rows="2" cols="50" name="DESCRIPTION"  placeholder="Description of the article" style="resize:none;"></textarea></p> 
        <p><input type="text" size="50" name="USERNAME" autocomplete="off" placeholder="Your nickname" pattern='[a-zA-Z]{2,25}' title="The name must be between 2 and 25 characters long" ></p>
        <p><input type="text" size="50" name="LINK" autocomplete="off" placeholder="Link to the article" title="An existing link must be entered" ></p>
        <p><input type="submit" value="Append"  class="btn btn-default"></p>        
</form>
