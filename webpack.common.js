const path = require('path');

module.exports = {
  mode: 'development',  // You can change to 'production' for production builds
  module: {
    rules: [
      {
        test: /\.css$/,  // Handle CSS files
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.js$/,  // Handle JavaScript files
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
          },
        },
      },
    ],
  },
  output: {
    path: path.resolve(__dirname, 'static/dist'),  // Output to a common directory
  },
};
