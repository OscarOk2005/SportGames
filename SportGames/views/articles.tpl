% rebase('layout.tpl', title=title, year=year)


<div class="container" id="container_forms">
     <h1 class="text-center">Articles</h1>

     <div class="row col-md-6">
        % for art in data:
            % for nameofarticle, details in art.items():
                <div class="col-md-12 col-sm-8">
                    <div class="panel-group">
                        <div class="panel panel-default">
                            <div class="panel-heading">
                                <h4 class="panel-title">
                                    <a data-toggle="collapse" href="#collapse{{nameofarticle}}">{{nameofarticle}}</a>
                                </h4>
                            </div>
                            <div id="collapse{{ nameofarticle }}" class="panel-collapse collapse collapse">
                                <div class="panel-body">
                                    <p><strong>Author: </strong>{{ details['author'] }}</p>
                                    <p  style="word-break:break-all" ><strong>Description: </strong>{{ details['text'] }}</p>
                                    <p><strong>Link: </strong> <a href="{{ details['link'] }}" target="_blank">{{ details['link'] }}</a></p>
                                    <p><strong>Date: </strong> {{ details['date'] }}</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            % end
        % end
    </div>
    <div class="input_container col-xs-4 col-sm-3 text-center">
        <h3> Adding an article</h3>
        <div class ="thumbnail">
            <form name="input_form" class="input_form" action="/articles" method="post" name="myForm"  required>
                <div class="form-group">
                    <input type="text" class="form-control input-sm" name="TITLE" autocomplete="off" placeholder="Title of the article"
                    title="The title of the article must contain at least 8 characters!">
                </div>
                <div class="form-group">
                    <textarea rows="2" cols="50" title="The description of the article must contain at least 20 characters!" name="DESCRIPTION" class="form-control input-sm"  placeholder="Description of the article" style="resize:none;"></textarea>
                </div>
                <div class="form-group">
                    <input type="text"  name="USERNAME" class="form-control input-sm" autocomplete="off" placeholder="Your nickname" 
                    title="The name must be between 2 and 20 characters long" >
                </div>
                <div class="form-group">
                    <input type="text" size="50" name="LINK" autocomplete="off" class="form-control input-sm" placeholder="Link to the article" title="An existing link must be entered" >
                </div>
                <div class="form-group">
                    <input type="text" size="50" name="DATE" autocomplete="off" class="form-control input-sm" placeholder="Date of creation of article" title="The date must be in the format 'dd.MM.yyyy'" >
                </div>
                <p><input type="submit" value="Append"  class="btn btn-default"></p>        
            </form>
        </div>
    </div>
</div>