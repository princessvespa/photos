import os, datetime

for file in os.listdir("./public/photos"):
    if file.endswith(".jpg"):
        date = datetime.datetime.fromtimestamp(int(os.path.getmtime(os.path.join("./public/photos", file)))).strftime('%Y-%m-%d');
        contents = "---\n" + "layout: post\n" + "title: " + file[:-4].title()+"\n" + "image: /public/photos/"+ file+ "\n" + "caption: \n" + "date: " + date +"\n" +  "tags: []\n" + "---";
        f = open(os.path.join("./public/photos", date + "-" + file[:-4] + ".md") ,'w')
        f.write(contents)
        f.close()