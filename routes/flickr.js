var log = require('log4js').getLogger('auth'),
	fs = require('fs');

var resJson = {imgUrl: []};

exports.getNews = function(req, res) {
	var page_id = req.body.page_id;
	fs.readFile('data/news/99_'+page_id + '.json', 'utf8', function (err, data) {
	  	if (err) {
	    	console.log('Error: ' + err);
	    	return;
	  	}
	  	res.send(data);
	});
}

exports.getPageInfo = function(req, res) {
	var page_id = req.body.page_id;
	fs.readFile('data/facebook/'+page_id + '.json', 'utf8', function (err, data) {
	  	if (err) {
	    	console.log('Error: ' + err);
	    	return;
	  	}
	  	res.send(data);
	});
}

exports.readFile = function(req, res) {
    var fileName = req.body.fileName;
	fs.readFile('data/flickr/99/'+fileName + '.json', 'utf8', function (err, data) {
		// data/flickrs/ID.json //TODO
	  if (err) {
	    console.log('Error: ' + err);
	    return;
	  }
	  data = JSON.parse(data);
	  photos = data.photos.photo
	  for(var i = 0 ; i < photos.length ;i++){
		resJson['imgUrl'][i]="http://farm"+photos[i].farm+".static.flickr.com/"+photos[i].server+"/"+photos[i].id+"_"+photos[i].secret+"_m.jpg"
		//webURL="http://www.flickr.com/photos/"+photos[i].owner+"/"+photos[i].id+"/sizes/s/"
	  }
	  //log.info(resJson.imgUrl);
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
