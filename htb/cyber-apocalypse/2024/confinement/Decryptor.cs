using System.Security.Cryptography;
using System.Text;

public class Decryptor {
    public string password { get; set; }

    public Decryptor(string password)
    {
        this.password = Hasher(password);
    }
    
    public string Hasher(string password)
    {
        using SHA512CryptoServiceProvider sHA512CryptoServiceProvider = new SHA512CryptoServiceProvider();
        byte[] bytes = Encoding.UTF8.GetBytes(password);
        return Convert.ToBase64String(sHA512CryptoServiceProvider.ComputeHash(bytes));
    }

    public void DecryptFile(string file)
    {
        byte[] array = new byte[65535];
        byte[] salt = new byte[8] { 0, 1, 1, 0, 1, 1, 0, 0 };
        Rfc2898DeriveBytes rfc2898DeriveBytes = new Rfc2898DeriveBytes(password, salt, 4953);
        RijndaelManaged rijndaelManaged = new RijndaelManaged();
        rijndaelManaged.Key = rfc2898DeriveBytes.GetBytes(rijndaelManaged.KeySize / 8);
        rijndaelManaged.Mode = CipherMode.CBC;
        rijndaelManaged.Padding = PaddingMode.ISO10126;
        rijndaelManaged.IV = rfc2898DeriveBytes.GetBytes(rijndaelManaged.BlockSize / 8);
        FileStream fileStream = null;
        try
        {
            fileStream = new FileStream(file, FileMode.Open, FileAccess.ReadWrite);
        }
        catch (Exception ex2)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(ex2.Message);
            Console.ForegroundColor = ConsoleColor.Red;
        }
        
        try
        {
            long position = fileStream.Position;
            int num2 = fileStream.ReadByte() ^ 0xFF;
            fileStream.Seek(position, SeekOrigin.Begin);
            fileStream.WriteByte((byte)num2);
            fileStream.Seek(0, SeekOrigin.Begin);
        }
        catch (Exception ex6)
        {
            Console.ForegroundColor = ConsoleColor.Red;
            Console.WriteLine(ex6.Message);
            Console.ForegroundColor = ConsoleColor.Red;
        }
        
        if (fileStream.Length < 1000000)
        {
            string path = null;
            FileStream fileStream2 = null;
            CryptoStream cryptoStream = null;
            try
            {
                path = file + ".dec";
                fileStream2 = new FileStream(path, FileMode.Create, FileAccess.Write);
                cryptoStream = new CryptoStream(fileStream2, rijndaelManaged.CreateDecryptor(), CryptoStreamMode.Write);
            }
            catch (Exception ex3)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine(ex3.Message);
                Console.ForegroundColor = ConsoleColor.Red;
            }
            try
            {
                int num;
                do
                {
                    num = fileStream.Read(array, 0, array.Length);
                    if (num != 0)
                    {
                        cryptoStream.Write(array, 0, num);
                    }
                }
                    while (num != 0);
                fileStream.Close();
                cryptoStream.Close();
                fileStream2.Close();
            }
            catch (Exception ex4)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine(ex4.Message);
                Console.ForegroundColor = ConsoleColor.Red;
            }
            try
            {
                return;
            }
            catch (Exception)
            {
                return;
            }
        }
        fileStream.Close();
    }
}