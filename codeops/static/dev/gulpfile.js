const gulp = require('gulp')
const babel = require('gulp-babel');
const livereload = require('gulp-livereload')
const minifyJS = require('gulp-minify')
const cleanCSS = require('gulp-clean-css');


// Conversion de l'ES6 avec Babel.
gulp.task('babel', function(){
    return gulp.src('src/index.js')
        .pipe(babel({
            presets: ['env']
        }))
        .pipe(minifyJS())
        .pipe(gulp.dest('../dist/js/'))
})

// On surveille la modification des fichiers.
gulp.task('css', function(){
    return gulp.src('src/*.css')
        .pipe(cleanCSS())
        .pipe(gulp.dest('../dist/css/'))
        .pipe(livereload())
})

gulp.task('watch', function(){
    livereload.listen()
    gulp.watch('src/*.css', ['css'])
    gulp.watch('src/*.js', ['babel'])
})

// Tâche par défaut.
gulp.task('default', ['watch'] , function(){
    console.log('Dev mode')
})

gulp.task('prod', ['babel'], function(){

})