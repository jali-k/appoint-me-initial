const { merge } = require('webpack-merge');
const common = require('../webpack.common.js');  // Import common config
const path = require('path');

module.exports = merge(common, {
  entry: './authentication/static/authentication/js/main.js',  // Entry point for auth app
  output: {
    filename: 'auth.bundle.js',  // Output file
    path: path.resolve(__dirname, 'static/dist'),  // Output path
  },
});
