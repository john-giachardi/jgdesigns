const gulp = require('gulp');
const sass = require('gulp-sass')(require('sass'));
const postcss = require('gulp-postcss');
const autoprefixer = require('autoprefixer');

gulp.task('compile-scss', function() {
  return gulp
    .src('jgdesigns/static/scss/style.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(postcss([autoprefixer()]))
    .pipe(gulp.dest('jgdesigns/static/css'));
});

gulp.task('watch', function() {
  gulp.watch('jgdesigns/static/scss/style.scss', gulp.series('compile-scss'));
});

gulp.task('default', gulp.series('compile-scss', 'watch'));
