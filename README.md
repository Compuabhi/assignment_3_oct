#APIs to test :-


## Insert posts into posts collection of lokal db
```
POST - http://localhost:5000/common/posts 
       payload = {
	        "title": "Test Title",
	        "description": "Test description",
	        "location":["Delhi","Mumbai"],
	        "category":["Education","Politics"]
       } 
```
-----

## Fetch filtered posts from posts collection of lokal db 

```
POST - http://localhost:5000/common/filterposts 
        payload  = {
                "location":{"filter_type":"or",
                    "values":["GandhiNagar","Delhi"]
                },
                "category":{"filter_type":"or",
                    "values":["National","Sports"]
                }
        }

        ---or--- 

        payload  = {
                "location":{"filter_type":"and",
                    "values":["Chennai","Delhi"]
                },
                "category":{"filter_type":"and",
                    "values":["Education","Politics"]
                }
        }
```        
###

## SourceCode Structure :-

* lokal/core/flask_wrapper_lokal - wrapper for api_handler
* lokal/core/services/post_handler - handler for posts_api                     
* lokal/core/controllers/post_controller - controller for posts_api             
                    

* lokal/common/db/post_db - core file for inserting posts into db and fetching filtered posts