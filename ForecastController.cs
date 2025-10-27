using Microsoft.AspNetCore.Mvc;

namespace eFinance.API.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public class ForecastController : ControllerBase
    {
        // GET api/forecast/sample
        [HttpGet("sample")]
        public IActionResult Sample()
        {
            var sample = new {
                model = "ARIMA",
                forecast_next_month = 150000.0M
            };
            return Ok(sample);
        }
    }
}
