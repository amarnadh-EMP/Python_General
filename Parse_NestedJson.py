import pandas as pd
from pandas import json_normalize
import json

df=pd.read_json('C:\\Users\\agunakala001\Desktop\python\Sighplan.json')
#tells us parent node is 'data'

#json_normalize copy whole col respective data as {} for those which mentioned in meta=[],
#Eg here ['data'] is root list and comments is nested list inside ['data'] to split along with meta=[] as seperate cols

Base=json_normalize(df['data'],'comments',meta=[
    'assigned',	'category',	'changeLog',	'completion',	'creation',	'customVars',	'description',	'dueDate',	'friendlyId',	'id',	'isCompleted',	'isOpen',	'isPastDue',	'isProject',	'isProjectTask',	'isRepeating',	'isTask',	'isUrgent',	'location',	'markerLatitude',	'markerLongitude',	'objectiveUrls',	'percentComplete',	'place',	'pmId',	'pmPropertyId',	'projectId',	'projectTaskCount',	'repeatingFrequency',	'repeatingName',	'residentChargeBack',	'status',	'subCategory',	'TaskTag',	'templateID',	'templateName',	'timetracking',	'workspace'

])
# comments, completion.documentation.documentation are nested objects inside Base
#to_json fn will make {a:1,b:2} from row into col a, b with 1, 2 as values in rows, but this fn won't look into list[],
#fn will take care those objects in rows & converts as rows 


new=pd.json_normalize(json.loads(Base.to_json(orient='records')))

#print(new)

Base.to_excel('neww1.xlsx')
