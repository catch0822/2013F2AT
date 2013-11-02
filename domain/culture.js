var config = require('../config'),
    redis = require("redis"),
    mongoose = require('mongoose'),
    mongooseRedisCache = require("mongoose-redis-cache"),
    Schema = mongoose.Schema;

var redisCulture = redis.createClient(config.redis.port, config.redis.host),
    mongoCulture = mongoose.connect('mongodb://localhost/iCulture');


var cultureSchema = new Schema({
    name:           {type: String, unique: true, required: true},
    address:        {type: String, required: true},
    longitude:      {type:Number, required: true},
    latitude:       {type:Number, required: true},
    openTime:       {type: String, required: true},
    closeDay:       {type: String},               
    mainTypeName:   {type: String},     
    cityName:       {type: String},     
    groupTypeName:  {type: String},     
    mainTypePk:     {type:Number, unique: true, required: true}
});

cultureSchema.pre('save', function (next) {
    next();
});

cultureSchema.set('redisCache', true);
cultureSchema.set('expires', 30000);

mongooseRedisCache(mongoose, {
   host: config.redis.host,
   port: config.redis.port
});

var CultureModel = mongoose.model('Culture', cultureSchema);

function Culture() {
    ;
}

Culture.cultureModel = function(){
    return CultureModel;
};

module.exports = Culture;