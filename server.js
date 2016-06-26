var http = require("http")
var sys = require('sys');
const exec = require('child_process').exec;

http.createServer(function(req, res) {
    res.setHeader('Access-Control-Allow-Origin', '*');
    res.setHeader('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS');
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type, Authorization, Content-Length, X-Requested-With');
    child = exec("python2 ~/Downloads/striiv_api_sample.py WzmWeTHjhF 8Fwye9pmJqqsmBpk eErmwAN6npsc4TBh", function(error, stdout, stderr) {
        res.end(stdout);
        if (error !== null) {
            console.log('exec error: ' + error);
        }
    });
}).listen(8080, 'localhost');
