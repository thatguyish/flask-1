### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?  
  -javascript uses `{}` where python uses `:` and indention to define code scope.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.  
  -`dicts.get('key-word')`  
  -`dicts.setdefault()`
- What is a unit test?  
  -Test that verify proper functionality of individual pieces of code.
- What is an integration test?  
  -Test that verify proper functionality of pieces of code that work together.
- What is the role of web application framework, like Flask?  
 -To make serving files over the web easier.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?  
  -If you wanted to create a seperate page like questions for a survey i would say use a url route for anything else use a query parameter.
- How do you collect data from a URL placeholder parameter using Flask?  
  -`url/<variable>` then use `variable` in your code as if it were the value you needed
- How do you collect data from the query string using Flask?  
  -`request.args('variable name')`
- How do you collect data from the body of the request using Flask?  
  -`request.form('variable name')`
- What is a cookie and what kinds of things are they commonly used for?  
  -A cookie is a small amount of data that persist allowing your web application to change states.
- What is the session object in Flask?  
  -The session object holds any data you'd like then stores it in a cookie for as long as the browser session is active.
- What does Flask's `jsonify()` do?  
  -It turns your data into a json object that can then be sent as any json data packet.
