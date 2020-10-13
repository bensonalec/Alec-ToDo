users = {
    "users": [
        {
            "username":"sample@sample.com",
            "passHash":"password12",
            "id":0
        },
        {
            "username":"sample2@sample.com",
            "passHash":"password34",
            "id":1
        },
        {
            "username":"donnieboy@sample.com",
            "passHash":"h4ng0utW1thM3M0r3",
            "id":2
        }
    ]
}

lists = {
    "lists": [
        {
            "id":0,
            "entries" : [
                {
                    "title":"sampleEntry",
                    "description":"A sample to do entry",
                    "date":"Never"
                },
                {
                    "title":"sampleEntry2",
                    "description":"A sample to do entry",
                    "date":"Never"
                }
            ]
        },
                {
            "id":1,
            "entries" : [
                {
                    "title":"sampleEntry",
                    "description":"A sample to do entry",
                    "date":"Never"
                }
            ]
        }
    ]
}
import pickle
pickle.dump(users,open("users.pickle","wb"))
pickle.dump(lists,open("lists.pickle","wb"))
