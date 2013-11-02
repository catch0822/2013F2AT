
/*
 * GET home page.
 */

exports.index = function(req, res){
  res.render('index.html');
};


exports.test = function(req, res){
  res.render('test_popular.html');
};

exports.test2 = function(req, res){
  res.render('test2.html');
};

exports.test_news = function(req, res){
  res.render('test_news.html');
};

exports.test_map = function(req, res){
  res.render('map.html');
};


exports.test_earth = function(req, res){
  res.render('earth.html');
};

exports.foot = function(req, res){
  res.render('foot.html');
};