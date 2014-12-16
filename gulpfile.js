var gulp = require('gulp');
var autoprefixer = require('gulp-autoprefixer');
var minifycss = require('gulp-minify-css');
var less = require('gulp-less');
var jshint = require('gulp-jshint');
var uglify = require('gulp-uglify');
var imagemin = require('gulp-imagemin');
var rename = require('gulp-rename');
var debug = require('gulp-debug');
var concat = require('gulp-concat');
var cache = require('gulp-cache');
var d = "./src/phenology.plone/src/phenology/plone/static/";
var lessfiles = [d+'less/_plone.less'];
var javascripts = [d+'js/theme.js'];
w = process.cwd();
styles = gulp.task(
    'styles',
    function() {
        return gulp.src(lessfiles)
        .pipe(less())
        .pipe(autoprefixer('last 2 version', 'safari 5', 'ie 8', 'ie 9', 'opera 12.1', 'ios 6', 'android 4'))
        .pipe(rename("theme.css"))
        .pipe(gulp.dest(d+'css/'))
        .pipe(minifycss())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest(d+'css/'));
    });
/*
js = gulp.task(
    'js',
    function() {
        return gulp.src(javascripts)
        .pipe(concat('script.js'))
        .pipe(gulp.dest(d+'js/'))
        .pipe(uglify())
        .pipe(rename('script.min.js'))
        .pipe(gulp.dest(d+'js/'));
    });
fonts = gulp.task(
    'fonts',
    function() {
        return gulp.src([
            './bower_components/font-awesome/fonts/**',
        ])
        .pipe(gulp.dest(d+'fonts/'));
    });
*/
gulp.task('default', ['styles']);
gulp.task('watch', function() {
  gulp.watch(lessfiles, ['styles']);
  /* gulp.watch(javascripts, ['js']); */
});
/* vim:set ft=javascript : */
