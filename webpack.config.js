const path = require('path');

module.exports = {
  entry: './assets/js/main.js', // Entry point for your frontend code
  output: {
    path: path.resolve(__dirname, 'static/dist'), // Where Webpack will output bundled files
    filename: 'bundle.js', // Name of the output file
  },
  module: {
    rules: [
      {
        test: /\.js$/, // Babel loader for JavaScript
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
      {
        test: /\.css$/, // CSS loader
        use: ['style-loader', 'css-loader'],
      },
    ],
  },
  devtool: 'source-map', // To help with debugging
};
