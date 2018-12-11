const path = require('path');


module.exports = {
    entry: ["@babel/polyfill", "./js/main.js"],
    output: {
        path: path.resolve(__dirname, 'js'),
        filename: 'main.bundle.js'
    },
    module: {
        rules: [
            {
                test: /\.js$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader'
                }
            }
        ]
    }
};