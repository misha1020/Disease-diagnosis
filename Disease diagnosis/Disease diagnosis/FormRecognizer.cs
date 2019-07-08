using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Diagnostics;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Disease_diagnosis
{
    public partial class FormRecognizer : Form
    {
        Bitmap image;
        string imageName;
        string modelName = "none";

        public FormRecognizer()
        {
            InitializeComponent();
        }

        private string Recognize()
        {
            string result;
            Process p = new Process();
            p.StartInfo.FileName = "python.exe";
            p.StartInfo.RedirectStandardOutput = true;
            p.StartInfo.UseShellExecute = false;
            p.StartInfo.Arguments = "MyData.py" + " \"" + modelName + "\"" + " \"" + imageName + "\"";
            p.StartInfo.CreateNoWindow = true;
            p.StartInfo.RedirectStandardError = true;
            p.Start();
            StreamReader s = p.StandardOutput; 
            string output = s.ReadToEnd();
            string[] r = output.Split(new char[] { '\r' });
            p.WaitForExit();

            if (r[0] == "Yes")
                result = "Онкология";
            else if (r[0] == "No")
                result = "Не онкология";
            else
                result = "Не удалось распознать";

            return result;
        }

        private void btLoadPhoto_Click(object sender, EventArgs e)
        {
            OpenFileDialog open_dialog = new OpenFileDialog(); //создание диалогового окна для выбора файла
            open_dialog.Filter = "Image Files(*.JPG)|*.JPG|All files (*.*)|*.*"; //формат загружаемого файла
            if (open_dialog.ShowDialog() == DialogResult.OK) //если в окне была нажата кнопка "ОК"
            {
                try
                {
                    imageName = open_dialog.FileName;
                    image = new Bitmap(imageName);
                    pbImage.Image = image;
                    pbImage.Invalidate();
                }
                catch
                {
                    DialogResult rezult = MessageBox.Show("Невозможно открыть выбранный файл", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
        }

        private void btLoadModel_Click(object sender, EventArgs e)
        {
            OpenFileDialog open_dialog = new OpenFileDialog(); //создание диалогового окна для выбора файла
            open_dialog.Filter = "Models(*.h5)|*.h5"; //формат загружаемого файла
            if (open_dialog.ShowDialog() == DialogResult.OK) //если в окне была нажата кнопка "ОК"
                    modelName = open_dialog.FileName;
        }

        private void btRecognize_Click(object sender, EventArgs e)
        {
            if (pbImage.Image == null)
                MessageBox.Show("Для распознаваня необходимо выбрать образ!", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
            else if (modelName == "none")
                MessageBox.Show("Для распознаваня необходимо выбрать обученную сеть!", "Ошибка", MessageBoxButtons.OK, MessageBoxIcon.Error);
            else
            {
                string result = Recognize();
                MessageBox.Show("Результат распознавания: " + result, "Постановка диагноза", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
        }
    }
}
