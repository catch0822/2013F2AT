var spawn = require('child_process').spawn,
    log = require('log4js').getLogger('triggerPython');

module.exports.start = function(uid, accessToken){
    log.info("uid: "+uid);
    log.info("accessToken: "+accessToken);
    //TODO: replace 'helloworld' to Prada's script, and pass accessToken and uid to him
    pythonProcess = spawn('python', ['src/helloworld.py']),

    pythonProcess.stdout.on('data', function(data) {
        log.info('stdout: ' + data);
    });

    pythonProcess.stderr.on('data', function (data) {
        log.info('stderr: ' + data);
    });

    pythonProcess.on('close', function (code) {
        log.info('child process exited with code ' + code);
    });
}