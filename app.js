var express = require('express'),
    routes = require('./routes'),
    flickr =require('./routes/flickr'),
    http = require('http'),
    path = require('path'),
    auth = require('./routes/auth');

var app = express();

app.set('port', 3000);
app.set('views', __dirname + '/views');
app.set('view engine', 'jade');
app.engine('html', require('ejs').renderFile); // set html
app.use(express.favicon());
app.use(express.logger('dev'));
app.use(express.bodyParser());
app.use(express.methodOverride());
app.use(app.router);
app.use(express.static(path.join(__dirname, 'public')));

if ('development' == app.get('env')) {
    app.use(express.errorHandler());
}

// URL Mapping
app.get('/', routes.index);
app.post('/flickr/readFile', flickr.readFile);
app.post('/flickr/exhibition_list', flickr.exhibition_list);
app.get('/test', routes.test);
app.get('/test2', routes.test2);
app.get('/foot', routes.foot);
app.get('/test_news', routes.test_news);
app.get('/test_map', routes.test_map);
app.get('/test_earth', routes.test_earth);

//app.post('/auth/fbLogin', auth.fbLogin);
http.createServer(app).listen(app.get('port'), function() {
    console.log('Starting web server at ' + app.get('port'));
});
