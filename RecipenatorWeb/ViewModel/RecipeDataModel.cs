using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ViewModel
{
    public class RecipeDataModel
    {
        public string Recipe { get; set; }
        public string Author { get; set; }
        public string Date { get; set; }
        public string Url { get; set; }
        public string Description { get; set; }
        public string UsrRating { get; set; }
        public string Servings { get; set; }
        public string Calories { get; set; }
        public string TotalTime { get; set;}
        public string Ingredients { get; set; }
        public string Instructions { get; set; }
    }
}
