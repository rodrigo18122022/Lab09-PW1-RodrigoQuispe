#!"C:\xampp\perl\bin\perl.exe"
use strict;
use warnings;
use CGI qw(:standard);
use CGI::Carp qw(fatalsToBrowser);

open my $fh, '<', 'C:\xampp\htdocs\Lab09-PW1-RodrigoQuispe\archivos\archivo.txt' or die $!;
our %universidades;

while (<$fh>) {
    chomp;
    my @campos = split /\|/;
    my $codigo_entidad = $campos[0];
    $universidades{$codigo_entidad} = $_;
}

close $fh;

if (param()) {
    print header,
          start_html('Prueba de Lectura y Almacenamiento en Diccionario'),
          h1('Contenido del Diccionario'),
          p(pre(join("\n", map { "$_ => $universidades{$_}" } keys %universidades))),
          end_html;
} else {
    print header,
          start_html('Prueba de Lectura y Almacenamiento en Diccionario'),
          h1('Prueba de Lectura y Almacenamiento en Diccionario'),
          start_form,
          p(submit),
          end_form,
          end_html;
}

