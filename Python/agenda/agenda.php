<?PHP
if(file_exists('agenda.json'))
{
	$filename = 'agenda.json';
	$data = file_get_contents($filename); //data read from json file
	//print_r($data);
	$contactos = json_decode($data);  //decode a data
	
	//print_r($contactos); //array format data printing
	 $message = "<h3 class='text-success'>Contactos</h3>";
}else{
	 $message = "<h3 class='text-danger'>Sin Contactos</h3>";
}
?>
<!DOCTYPE html>
 <html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:400,700">
  <title>Contactos</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
<script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>

<style>
#tbstyle {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 50%;
}

#tbstyle td, #tbstyle th {
  border: 1px solid 
#ddd;
  padding: 8px;
}

#tbstyle tr:nth-child(even){background-color: 
#f2f2f2;}

#tbstyle tr:hover {background-color: 
#ddd;}

#tbstyle th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: left;
  background-color: 
#859161;
  color: 
White;
}
</style>
      </head>
	  <body>
	   <div class="container" style="width:500px;">
	   <div class="table-container">
	   <?php
			 if(isset($message))
			 {
				  echo $message;

			 ?>
		<table id="tbstyle">
			<tbody>
				<tr>
					<th>Nombre</th>
					<th>Telefonos</th>
					<th>Correo</th>
					<th>Direccion</th>
					<th>Ciudad</th>
				</tr>
				<?php foreach ($contactos as $contacto) { ?>
				<tr>
					<td> <?= $contacto->nombre; ?> </td>
					<td> <?= $contacto->telefono; ?> </td>
					<td> <?= $contacto->correo; ?> </td>
					<td> <?= $contacto->direccion; ?> </td>
					<td> <?= $contacto->ciudad; ?> </td>
				</tr>
				<?php }
			 }
			 else
				echo $message;
			 ?>
    </tbody>
</table>
</div>
</div>
</body>
</html>