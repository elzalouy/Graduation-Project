using Microsoft.Owin;
using Owin;

[assembly: OwinStartupAttribute(typeof(Life.Startup))]
namespace Life
{
    public partial class Startup
    {
        public void Configuration(IAppBuilder app)
        {
            ConfigureAuth(app);
        }
    }
}
