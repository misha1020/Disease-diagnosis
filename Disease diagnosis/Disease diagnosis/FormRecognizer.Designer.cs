namespace Disease_diagnosis
{
    partial class FormRecognizer
    {
        /// <summary>
        /// Обязательная переменная конструктора.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Освободить все используемые ресурсы.
        /// </summary>
        /// <param name="disposing">истинно, если управляемый ресурс должен быть удален; иначе ложно.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Код, автоматически созданный конструктором форм Windows

        /// <summary>
        /// Требуемый метод для поддержки конструктора — не изменяйте 
        /// содержимое этого метода с помощью редактора кода.
        /// </summary>
        private void InitializeComponent()
        {
            this.btLoadPhoto = new System.Windows.Forms.Button();
            this.btRecognize = new System.Windows.Forms.Button();
            this.pbImage = new System.Windows.Forms.PictureBox();
            this.btLoadModel = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.pbImage)).BeginInit();
            this.SuspendLayout();
            // 
            // btLoadPhoto
            // 
            this.btLoadPhoto.Location = new System.Drawing.Point(12, 61);
            this.btLoadPhoto.Name = "btLoadPhoto";
            this.btLoadPhoto.Size = new System.Drawing.Size(300, 44);
            this.btLoadPhoto.TabIndex = 0;
            this.btLoadPhoto.Text = "Загрузить изображение";
            this.btLoadPhoto.UseVisualStyleBackColor = true;
            this.btLoadPhoto.Click += new System.EventHandler(this.btLoadPhoto_Click);
            // 
            // btRecognize
            // 
            this.btRecognize.Location = new System.Drawing.Point(12, 342);
            this.btRecognize.Name = "btRecognize";
            this.btRecognize.Size = new System.Drawing.Size(300, 55);
            this.btRecognize.TabIndex = 1;
            this.btRecognize.Text = "Распознать загруженный образ";
            this.btRecognize.UseVisualStyleBackColor = true;
            this.btRecognize.Click += new System.EventHandler(this.btRecognize_Click);
            // 
            // pbImage
            // 
            this.pbImage.Location = new System.Drawing.Point(12, 111);
            this.pbImage.Name = "pbImage";
            this.pbImage.Size = new System.Drawing.Size(300, 225);
            this.pbImage.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pbImage.TabIndex = 2;
            this.pbImage.TabStop = false;
            // 
            // btLoadModel
            // 
            this.btLoadModel.Location = new System.Drawing.Point(12, 11);
            this.btLoadModel.Name = "btLoadModel";
            this.btLoadModel.Size = new System.Drawing.Size(300, 44);
            this.btLoadModel.TabIndex = 3;
            this.btLoadModel.Text = "Загрузить обученную сеть";
            this.btLoadModel.UseVisualStyleBackColor = true;
            this.btLoadModel.Click += new System.EventHandler(this.btLoadModel_Click);
            // 
            // FormRecognizer
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(324, 405);
            this.Controls.Add(this.btLoadModel);
            this.Controls.Add(this.pbImage);
            this.Controls.Add(this.btRecognize);
            this.Controls.Add(this.btLoadPhoto);
            this.Name = "FormRecognizer";
            this.Text = "Диагностика заболеваний";
            ((System.ComponentModel.ISupportInitialize)(this.pbImage)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btLoadPhoto;
        private System.Windows.Forms.Button btRecognize;
        private System.Windows.Forms.PictureBox pbImage;
        private System.Windows.Forms.Button btLoadModel;
    }
}

