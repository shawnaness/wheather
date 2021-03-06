const webpack = require('webpack');
var ExtractTextPlugin = require('extract-text-webpack-plugin');

const config = {
	entry: {
		home: __dirname + '/js/index.jsx',
		submit: __dirname + '/js/submit.jsx'
	},
	output: {
		path: __dirname + "/dist",
		filename: '[name].bundle.js'
	},
	resolve: {
		extensions: ['.js', '.jsx', '.css']
	},
	module: {
	  rules: [
	    {
	    test: /\.jsx?/,
	    exclude: /node_modules/,
	    use: 'babel-loader'
	    },
		{
		  test: /\.css$/,
		  use: ExtractTextPlugin.extract({
		         fallback: 'style-loader',
		         use: 'css-loader',
		       })
		},
		{		
		  test: /\.(png|svg|jpg|gif)$/,
		  use: 'file-loader'
		}
	  ]
	},
	plugins: [  
		new ExtractTextPlugin('styles.css')
		]
};


module.exports = config;