var log = require('log4js').getLogger('auth'),
    triggerPython = require('../src/triggerPython');

exports.fbLogin = function(req, res) {
    var tokenInfo = req.body.tokenInfo;
    log.info("uid: "+tokenInfo.uid);
    log.info("accessToken: "+tokenInfo.accessToken);
    res.send(req.body);
    triggerPython.start(tokenInfo.uid, tokenInfo.accessToken);
};