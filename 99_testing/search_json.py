import json

sampleJson = """{ 
   "class":{ 
      "student":{ 
         "name":"jhon",
         "marks":{ 
            "physics": 70,
            "mathematics": 80
         },
         "subjects": ["sub1", "sub2", "sub3", "sub4"]
      }
   }
}"""
sampleDict = json.loads(sampleJson)
if 'class' in sampleDict:
    if 'student' in sampleDict['class']:
        if 'subjects' in sampleDict['class']['student']:
            print("Iterating JSON array")
            for sub in sampleDict['class']['student']['subjects']:
                print(sub)