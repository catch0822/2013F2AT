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