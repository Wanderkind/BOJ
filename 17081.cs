#pragma warning disable CS8602, CS8603, CS8618

namespace RPG_Extreme
{
    public class Monster
    {
        public int Row { get; set; }
        public int Col { get; set; }
        public string Name { get; set; }
        public int Atk { get; set; }
        public int Def { get; set; }
        public int Hp { get; set; }
        public int ExpDrop { get; set; }

        public Monster(int row, int col, string name,
            int atk, int def, int hp, int exp)
        {
            Row = row; Col = col; Name = name;
            Atk = atk; Def = def; Hp = hp; ExpDrop = exp;
        }
    }

    public interface IBox
    {
        int Row { get; set; }
        int Col { get; set; }
        int IBox_Val();
    }
    public class WBox : IBox
    {
        public int Row { get; set; }
        public int Col { get; set; }
        public int Val { get; set; }

        public WBox(int row, int col, int val)
        {
            Row = row; Col = col; Val = val;
        }

        public int IBox_Val()
        {
            return Val;
        }
    }
    public class ABox : IBox
    {
        public int Row { get; set; }
        public int Col { get; set; }
        public int Val { get; set; }

        public ABox(int row, int col, int val)
        {
            Row = row; Col = col; Val = val;
        }

        public int IBox_Val()
        {
            return Val;
        }
    }
    public class OBox : IBox
    {
        public int Row { get; set; }
        public int Col { get; set; }
        public string Type { get; set; }

        public OBox(int row, int col, string type)
        {
            Row = row; Col = col; Type = type;
        }

        public int IBox_Val()
        {
            if (Type == "HR") return 1;
            if (Type == "RE") return 2;
            if (Type == "CO") return 3;
            if (Type == "EX") return 4;
            if (Type == "DX") return 5;
            if (Type == "HU") return 6;
            return 0;
        }
    }

    public class Monster_Lib
    {
        private List<Monster> Monsters { get; }
        public Monster_Lib()
        {
            Monsters = new List<Monster>();
        }
        public void AddMonster(Monster monster)
        {
            Monsters.Add(monster);
        }
        public Monster FindMonster(int row, int col)
        {
            return Monsters.Find(mon => mon.Row == row && mon.Col == col);
        }
    }

    public class Box_Lib
    {
        private List<IBox> Boxes { get; }
        public Box_Lib()
        {
            Boxes = new List<IBox>();
        }
        public void AddBox(IBox box)
        {
            Boxes.Add(box);
        }
        public IBox FindBox(int row, int col)
        {
            return Boxes.Find(box => box.Row == row && box.Col == col);
        }
    }

    public class Battle
    {
        public int Prot_Hp { get; set; }
        public int Prot_total_Atk { get; set; }
        public int Prot_total_Def { get; set; }
        public bool Prot_courage { get; set; }
        public bool Prot_dexterity { get; set; }
        public bool Prot_hunter { get; set; }

        public int Mon_Hp { get; set; }
        public int Mon_Atk { get; set; }
        public int Mon_Def { get; set; }
        public int Mon_Exp { get; set; }
        public bool Mon_boss { get; set; }

        public Battle(int ph, int pa, int pd, bool pc, bool px, bool pt,
            int mh, int ma, int md, int me, bool mb)
        {
            Prot_Hp = ph; Prot_total_Atk = pa; Prot_total_Def = pd; Prot_courage = pc;
            Prot_dexterity = px; Prot_hunter = pt;  Mon_Hp = mh; Mon_Atk = ma;
            Mon_Def = md; Mon_Exp = me; Mon_boss = mb;
        }

        private readonly Func<int, int> apd = x => x > 1 ? x : 1;

        public int[] Battle_result()
        {
            for (int battle_turn = 0; ; battle_turn++)
            {
                if (battle_turn == 0)
                {
                    Mon_Hp -= apd((Prot_courage ?
                        (Prot_dexterity ? 3 : 2) : 1) * Prot_total_Atk - Mon_Def);
                    if (Mon_Hp < 1) break;
                    if (Prot_hunter && Mon_boss) continue;
                    Prot_Hp -= apd(Mon_Atk - Prot_total_Def);
                    if (Prot_Hp < 1) break;
                }
                else
                {
                    Mon_Hp -= apd(Prot_total_Atk - Mon_Def);
                    if (Mon_Hp < 1) break;
                    Prot_Hp -= apd(Mon_Atk - Prot_total_Def);
                    if (Prot_Hp < 1) break;
                }
            }
            int[] result = new int[2];
            result[0] = Prot_Hp; result[1] = Mon_Exp;
            return result;
        }
    }

    class Program
    {
        static void Main()
        {
            StreamReader sr = new(new BufferedStream(Console.OpenStandardInput()));
            StreamWriter sw = new(new BufferedStream(Console.OpenStandardOutput()));

            int N, M, K = 0, L = 0, r, c;
            int startr = 0, startc = 0;
            string str;
            string[] splt;
            char[] charr;
            
            splt = sr.ReadLine().Split();
            N = int.Parse(splt[0]);
            M = int.Parse(splt[1]);
            char[][] grid = new char[N][];
            for (int i = 0; i < N; i++)
            {
                charr = sr.ReadLine().ToCharArray();
                for (int j = 0; j < M; j++)
                {
                    if (charr[j] == '&' || charr[j] == 'M') K++;
                    else if (charr[j] == 'B') L++;
                    else if (charr[j] == '@')
                    {
                        startr = i; startc = j;
                    }
                }
                grid[i] = charr;
            }

            char[] moves = sr.ReadLine().ToCharArray();
            int len = moves.Length;

            Monster_Lib monster_lib = new();
            Box_Lib box_lib = new();
            for (int i = 0; i < K; i++)
            {
                splt = sr.ReadLine().Split();
                r = int.Parse(splt[0]) - 1;
                c = int.Parse(splt[1]) - 1;
                monster_lib.AddMonster(new Monster(r, c, splt[2], int.Parse(splt[3]),
                    int.Parse(splt[4]), int.Parse(splt[5]), int.Parse(splt[6])));
            }
            for (int i = 0; i < L; i++)
            {
                splt = sr.ReadLine().Split();
                r = int.Parse(splt[0]) - 1;
                c = int.Parse(splt[1]) - 1;
                str = splt[2];
                if (str == "W")
                {
                    box_lib.AddBox(new WBox(r, c, int.Parse(splt[3])));
                }
                else if (str == "A")
                {
                    box_lib.AddBox(new ABox(r, c, int.Parse(splt[3])));
                }
                else
                {
                    box_lib.AddBox(new OBox(r, c, splt[3]));
                }
            }
            
            sr.Close();

            int Hp = 20;
            int Hp_max = 20;
            int innate_Atk = 2;
            int innate_Def = 2;
            int Level = 1;
            int Exp = 0;

            int weapon_Atk = 0;
            int armor_Def = 0;

            int o_cnt = 0;
            bool hp_regen = false;
            bool resurrect = false;
            bool courage = false;
            bool exp_boost = false;
            bool dexterity = false;
            bool hunter = false;

            bool alive = true;
            bool complete = false;

            IBox box;
            Monster mon;
            Battle bat;

            char direction, cell;
            int u, v;
            bool b;
            int[] res;
            string killedby = "";

            r = startr; c = startc;
            grid[r][c] = '.';
            int turn = 0;
            for (; turn < len; turn++)
            {
                direction = moves[turn];
                if (direction == 'R') c++;
                else if (direction == 'L') c--;
                else if (direction == 'U') r--;
                else r++;

                if (r < 0 || N <= r || c < 0 || M <= c || grid[r][c] == '#')
                {
                    if (direction == 'R') c--;
                    else if (direction == 'L') c++;
                    else if (direction == 'U') r++;
                    else r--;
                }
                cell = grid[r][c];
                if (cell == '.') continue;

                if (cell == '^')
                {
                    Hp -= dexterity ? 1 : 5;
                    if (Hp < 1)
                    {
                        if (resurrect)
                        {
                            Hp = Hp_max;
                            resurrect = false;
                            o_cnt--;
                            r = startr; c = startc;
                        }
                        else
                        {
                            Hp = 0;
                            killedby = "SPIKE TRAP";
                            alive = false;
                            break;
                        }
                    }
                }
                
                else if (cell == 'B')
                {
                    box = box_lib.FindBox(r, c);
                    v = box.IBox_Val();
                    if (box is WBox) weapon_Atk = v;
                    else if (box is ABox) armor_Def = v;
                    else if (o_cnt < 4)
                    {
                        if (v == 1) { if (!hp_regen) { hp_regen = true; o_cnt++; } }
                        else if (v == 2) { if (!resurrect) { resurrect = true; o_cnt++; } }
                        else if (v == 3) { if (!courage) { courage = true; o_cnt++; } }
                        else if (v == 4) { if (!exp_boost) { exp_boost = true; o_cnt++; } }
                        else if (v == 5) { if (!dexterity) { dexterity = true; o_cnt++; } }
                        else if (v == 6) { if (!hunter) { hunter = true; o_cnt++; } }
                        else o_cnt++;
                    }
                    grid[r][c] = '.';
                }
                
                else
                {
                    b = cell == 'M';
                    mon = monster_lib.FindMonster(r, c);
                    if (b && hunter) Hp = Hp_max;
                    bat = new Battle(Hp, innate_Atk + weapon_Atk, innate_Def + armor_Def,
                        courage, dexterity, hunter, mon.Hp, mon.Atk, mon.Def, mon.ExpDrop, b);
                    res = bat.Battle_result();
                    u = res[0]; v = res[1];
                    if (u < 1)
                    {
                        if (resurrect)
                        {
                            Hp = Hp_max;
                            resurrect = false;
                            o_cnt--;
                            r = startr; c = startc;
                        }
                        else
                        {
                            Hp = 0;
                            killedby = mon.Name;
                            alive = false;
                            break;
                        }
                    }
                    else
                    {
                        Hp = u;
                        if (hp_regen) Hp = (Hp + 4 > Hp_max ? Hp_max : Hp + 3);
                        Exp += exp_boost ? 6 * v / 5 : v;
                        if (Exp >= 5 * Level)
                        {
                            Exp = 0;
                            Hp_max += 5;
                            Hp = Hp_max;
                            innate_Atk += 2;
                            innate_Def += 2;
                            Level++;
                        }
                        grid[r][c] = b ? '@' : '.';
                        if (b) { complete = true; break; }
                    }
                }
            }
            
            if (alive ^ complete) grid[r][c] = '@';
            foreach (char[] row in grid)
            {
                str = new string(row);
                sw.WriteLine(str);
            }
            if (alive ^ complete)
            {
                sw.WriteLine($"Passed Turns : {turn}\nLV : {Level}");
                sw.WriteLine($"HP : {Hp}/{Hp_max}\nATT : {innate_Atk}+{weapon_Atk}");
                sw.WriteLine($"DEF : {innate_Def}+{armor_Def}\nEXP : {Exp}/{5 * Level}");
                sw.WriteLine("Press any key to continue.");
            }
            else
            {
                sw.WriteLine($"Passed Turns : {turn + 1}\nLV : {Level}");
                sw.WriteLine($"HP : {Hp}/{Hp_max}\nATT : {innate_Atk}+{weapon_Atk}");
                sw.WriteLine($"DEF : {innate_Def}+{armor_Def}\nEXP : {Exp}/{5 * Level}");
                sw.WriteLine(complete ? "YOU WIN!" : $"YOU HAVE BEEN KILLED BY {killedby}..");
            }
            
            sw.Close();
        }
    }
}
