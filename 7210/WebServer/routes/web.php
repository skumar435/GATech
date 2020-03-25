<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/
//
// Route::get('captcha-form', 'CaptchaController@captchForm');
// Route::post('store-captcha-form', 'CaptchaController@storeCaptchaForm');

Route::get('/', function () {
    return view('welcome');
});

Route::get('/index', function () {
    return view('index');
});

Route::get('/test', function () {
    return view('transition');
});

Route::get('/assemble', function () {
    return view('geno-ass');
});

Route::get('/phylo', function () {
    return view('phylo');
});

// Route::get('geno-ass', 'FastaUploadController@fastaUpload')->name('fasta.upload');
//
// Route::post('geno-ass', 'FastaUploadController@fastaUploadPost')->name('fasta.upload.post');

Route::get('gene-pred', 'FastaUploadController@fastaUpload')->name('fasta.upload');

Route::get('comp-geno', 'FastaUploadController@fastaUploadCG')->name('fasta.uploadcg');

Route::post('execute/{id}', 'FastaUploadController@fastaUploadPost')->name('fasta.upload.post');

// Route::get('func-anno', 'FastaUploadController@fastaUpload')->name('fasta.upload');
//
// Route::post('func-anno', 'FastaUploadController@fastaUploadPost')->name('fasta.upload.post');
//
// Route::get('comp-geno', 'FastaUploadController@fastaUpload')->name('fasta.upload');
//
// Route::post('comp-geno', 'FastaUploadController@fastaUploadPost')->name('fasta.upload.post');

Route::get('gene-pred-execute/{fasta}', 'FastaUploadController@invoke_gene_pred');

Route::get('mail', 'MailController@send')->name('mail.send');
