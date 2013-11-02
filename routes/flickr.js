var log = require('log4js').getLogger('auth'),
	fs = require('fs');

var count = 20;
var resJson = {imgUrl: []};

exports.readFile = function(req, res) {
    var fileName = req.body.fileName;
	fs.readFile('src/target/'+fileName, 'utf8', function (err, data) {
	  if (err) {
	    console.log('Error: ' + err);
	    return;
	  }
	  data = JSON.parse(data);
	  for(var i = 0;i < count ;i++){
	  	photos = data.photos.photo
		resJson['imgUrl'][i]="http://farm"+photos[i].farm+".static.flickr.com/"+photos[i].server+"/"+photos[i].id+"_"+photos[i].secret+"_m.jpg"
	
		//webURL="http://www.flickr.com/photos/"+photos[i].owner+"/"+photos[i].id+"/sizes/s/"
	  }
	  log.info(resJson.imgUrl);
	  res.send(resJson);
	});
};

exports.exhibition_list = function(req, res) {
	retJson = {imgUrl: [], image_selected:[], friend_images:[], checkin_users:[], users:[]};
	var fb_uid = req.body.uid;
	fs.readFile('data/list/'+fb_uid+'.json', 'utf8', function (err, data) {
	   if (err) {
	    console.log('Error: ' + err);
	    return;
	   }
	   data = JSON.parse(data);
	   for(var i = 0;i < 9 ;i++){
	   	 image_url=data[''+i].image_url
	   	 image_selected=data[''+i].image_selected
	   	 friend_images=data[''+i].friend_images
	   	 checkin_users=data[''+i].checkin_users
	   	 users=data[''+i].users
	   	 retJson['imgUrl'][i]=image_url;
	   	 retJson['image_selected'][i]=image_selected;
		 retJson['friend_images'][i]=friend_images;
		 retJson['checkin_users'][i]=checkin_users;
		 retJson['users'][i]=users;
	  }
	  	res.send(retJson);
	});	
}