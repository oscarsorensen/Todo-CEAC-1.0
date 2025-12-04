
select * from emails
left join personas
on emails.personas = personas.identificador;