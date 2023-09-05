module.exports = {
    plugins: [
      require('autoprefixer')({
        overrideBrowserslist: [
          "last 4 versions",
          "> 1%",
          "ie >= 11"
        ]
      })
    ]
  }