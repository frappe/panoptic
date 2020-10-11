module.exports = {
	future: {
		removeDeprecatedGapUtilities: true,
		purgeLayersByDefault: true,
	},
	purge: {
		mode: 'all',
		enabled: process.env.FRAPPE_ENV === 'production',
		content: [
			'./panoptic/templates/**/*.html',
			'./panoptic/www/**/*.html'
		],
	},
	theme: {
		typography: {
			default: {
				css: {
					color: '#FFFFFF',
					a: {
						color: '#E37A30',
						'&:hover': {
							color: '#CB5B27',
						},
					},
				},
			},
		},
		extend: {},
		borderColor: theme => ({
			// default: '#60D6D7',
			default: '#90E2E3',
			orange: '#CB5B27',
		}),
		container: {
			center: true,
		},
		colors: {
			'white': '#FFFFFF',
			'black': '#000000',
			'teal-blue': {
				50: '#F3F5F7',
				100: '#E8ECEE',
				200: '#C5CFD5',
				300: '#A2B3BC',
				400: '#5D7989',
				500: '#174057',
				600: '#153A4E',
				700: '#0E2634',
				800: '#0A1D27',
				900: '#07131A',
			},
			'aqua-blue': {
				50: '#F7FDFD',
				100: '#EFFBFB',
				200: '#D7F5F5',
				300: '#BFEFEF',
				400: '#90E2E3',
				500: '#60D6D7',
				600: '#56C1C2',
				700: '#3A8081',
				800: '#2B6061',
				900: '#1D4041',
			},
			'panoptic-blue': {
				50: '#F2F3F5',
				100: '#E6E8EC',
				200: '#C0C5CF',
				300: '#9BA3B1',
				400: '#4F5D77',
				500: '#04183D',
				600: '#041637',
				700: '#020E25',
				800: '#020B1B',
				900: '#010712',
			},
			'orange': {
				50: '#FEF7F4',
				100: '#FCF0EA',
				200: '#F8D9CA',
				300: '#F3C1AA',
				400: '#EB936B',
				500: '#E2652B',
				600: '#CB5B27',
				700: '#883D1A',
				800: '#662D13',
				900: '#441E0D',
			},
		}
	},
	variants: {},
	plugins: [
		require('@tailwindcss/typography'),
	],
}
