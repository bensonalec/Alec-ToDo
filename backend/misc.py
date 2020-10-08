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