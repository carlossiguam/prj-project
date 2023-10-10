import React, { useState } from 'react';
import { Document, Packer, Paragraph, TextRun } from 'docx';

function Editor() {
  // Estado para almacenar el valor del input
  const [fileName, setFileName] = useState('');

  const handleFileNameChange = (event) => {
    // Actualiza el estado con el valor del input
    setFileName(event.target.value);
  };
  
  const createDoc = () => {
    // Crea un nuevo documento de docx
    const doc = new Document({
      sections: [
        {
          properties: {},
          children: [
            new Paragraph({
              children: [
                new TextRun("Hello World"),
                new TextRun({
                  text: "Foo Bar",
                  bold: true,
                }),
                new TextRun({
                  text: "\tGithub is the best",
                  bold: true,
                }),
              ],
            }),
          ],
        },
      ],
    });


    // Convierte el documento en un blob para descarga
    Packer.toBlob(doc).then((blob) => {
      // Crea una URL para el blob
      const url = URL.createObjectURL(blob);

      // Crea un enlace de descarga y establece el nombre del archivo
      const a = document.createElement('a');
      a.href = url;
      // Usa el nombre del archivo ingresado en el input y agrega la extensión .docx
      a.download = `${fileName}.docx`;
      a.style.display = 'none';
      document.body.appendChild(a);
      a.click();

      // Limpia la URL creada
      URL.revokeObjectURL(url);
    });
  };

  return (
    <div>
      <h1>-----</h1>
      {/* Input controlado por el estado */}
      <input
        type='text'
        id='fdocname'
        name='fdocname'
        value={fileName}
        onChange={handleFileNameChange}
        placeholder='Nombre del archivo'
      />
      <h1>-----</h1>
      <button type='button' onClick={createDoc}>Create Doc</button>
    </div>
  );
}

export default Editor;
